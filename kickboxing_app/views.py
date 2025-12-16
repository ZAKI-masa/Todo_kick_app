from django.shortcuts import render
from django.views import generic
from .models import ActionPlan,Article
from django.urls import reverse_lazy
from    django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views import View
from django.shortcuts import get_object_or_404
# Create your views here.



def index(request):

    return render(request,"kickboxing_app/index.html")


class IndexPlanView(generic.ListView):
    model=ActionPlan
    template_name='kickboxing_app/index_plan.html'


class DetailPlanView(generic.DetailView):
    model=ActionPlan
    template_name='kickboxing_app/ActionPlan_detail.html'


class CreatePlanView(generic.CreateView):
    model=ActionPlan
    template_name='kickboxing_app/ActionPlan_form.html'
    fields=['title','target_data','is_done','author','reason']


class UpdatePlanView(generic.UpdateView):
    model=ActionPlan
    template_name='kickboxing_app/ActionPlan_form.html'
    fields=['title','target_data','is_done','author','reason']

    def form_valid(self,form):
        before_done=self.get_object().is_done
        response=super().form_valid(form)
        if (not before_done) and self.object.is_done:
            # 完了していなかったものが完了になったとき 削除するかの確認ページに移動後　に確定ボタンを押すとプランを削除する
            return redirect('kickboxing_app:plan_done_confirm',pk=self.object.pk)
        return response
    
class DeletePlanConfirmView(generic.DeleteView):
    model=ActionPlan
    template_name='kickboxing_app/ActionPlan_delete_confirm.html'
    success_url=reverse_lazy('kickboxing_app:plan_index')
            


class DoneConfirmView(View):
    template_name = "kickboxing_app/ActionPlan_done_confirm.html"

    def get(self, request, pk):
        plan = get_object_or_404(ActionPlan, pk=pk)
        return render(request, self.template_name, {"object": plan})

    def post(self, request, pk):
        plan = get_object_or_404(ActionPlan, pk=pk)
        decision = request.POST.get("decision")

        if decision == "keep":
            # 残す（何もしない）
            # 残す（完了フラグを元に戻す）
            plan.is_done = False
            plan.save(update_fields=["is_done"])
            return redirect("kickboxing_app:plan_detail", pk=plan.pk)

        if decision == "delete":
            plan.delete()
            return redirect("kickboxing_app:plan_index")

        # 想定外は同じ画面に戻す
        return redirect("kickboxing_app:plan_done_confirm", pk=plan.pk)
        return redirect("kickboxing_app:plan_done_confirm", pk=plan.pk)
