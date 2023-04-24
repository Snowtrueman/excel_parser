from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView
from .forms import InputForm
from .parser import Parser
from .utils import DataPrinter


class IndexView(FormView):
    template_name = "parser/index.html"
    form_class = InputForm

    def get_initial(self):
        return self.kwargs.get("form")

    def post(self, request, *args, **kwargs):
        form = InputForm(request.POST, request.FILES)
        if form.is_valid():
            date_1 = form.cleaned_data.get("date_1")
            date_2 = form.cleaned_data.get("date_2")
            if "upload" in request.POST:
                parser = Parser(form.cleaned_data.get("file"), date_1, date_2)
                result = parser.get_parsed_data()
                if result is True:
                    return redirect(f"{reverse_lazy('result')}?date_1={date_1}&date_2={date_2}")
                else:
                    form.add_error("file", result["error"])
                    return render(request, "parser/index.html", context={"form": form})
            elif "info" in request.POST:
                return redirect(f"{reverse_lazy('result')}?date_1={date_1}&date_2={date_2}")
        else:
            return render(request, "parser/index.html", context={"form": form})


class ResultView(TemplateView):
    template_name = "parser/result.html"

    def get_context_data(self):
        context = super().get_context_data()
        printer = DataPrinter(self.request.GET.get("date_1"), self.request.GET.get("date_2"))
        context["data"] = printer.get_data()
        context["aggregated_data"] = printer.get_aggregated_data()
        return context
