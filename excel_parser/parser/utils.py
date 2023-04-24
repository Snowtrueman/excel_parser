from django.db.models import Sum, Q

from .models import Data


class DataPrinter:
    def __init__(self, date_1, date_2):
        self.date_1 = date_1
        self.date_2 = date_2
        self.data = {}
        self.aggregate_data = {}
        self.prefix_list = ["qliq", "qoil"]
        self.data_types = {"0": "fact", "1": "forecast"}

    def compile_data_by_date(self):
        for date_id in ["date_1", "date_2"]:
            date = self.__getattribute__(date_id)
            query = Data.objects.filter(date=date).all()
            if not query:
                return None
            for item in query:
                if item.company_id not in self.data:
                    self.data[item.company_id] = {"company_id": item.company_id, "company_name": item.company_name}
                if item.data_type == "0":
                    self.data[item.company_id][f"fact_qliq_{date_id}"] = item.qliq
                    self.data[item.company_id][f"fact_qoil_{date_id}"] = item.qoil
                elif item.data_type == "1":
                    self.data[item.company_id][f"forecast_qliq_{date_id}"] = item.qliq
                    self.data[item.company_id][f"forecast_qoil_{date_id}"] = item.qoil
        return True

    def compile_aggregated_data(self):
        for date_id in ["date_1", "date_2"]:
            date = self.__getattribute__(date_id)
            for prefix in self.prefix_list:
                for data_type in self.data_types.keys():
                    result = Data.objects.aggregate(sum=Sum(f"{prefix}", filter=Q(date=date, data_type=data_type)))
                    if result["sum"]:
                        self.aggregate_data[f"{self.data_types[data_type]}_{prefix}_{date_id}"] = result
                    else:
                        return None
        return True

    def get_data(self):
        result = self.compile_data_by_date()
        if result:
            return list(self.data.values())

    def get_aggregated_data(self):
        result = self.compile_aggregated_data()
        if result:
            return self.aggregate_data
