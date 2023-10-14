from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import View, ListView
from .forms import PlayerCreationForm, PlayerForm
from .models import Player


class PlayerCreateUpdateBaseView(View):
    """ Create update player base view. """

    menu_name = "Players"
    submenu_name = "Player"
    action_name = "Update/Add player"
    button_name = "Save"

    model = Player
    form_class = PlayerForm

    template_name = "player_update_form.html"

    def get_context_data(self, **kwargs):
        data = dict()
        data["menu_name"] = self.menu_name
        data["submenu_url"] = self.get_success_url()
        data["submenu_name"] = self.submenu_name
        data["action_name"] = self.action_name
        data["button_name"] = self.button_name
        return data

    def get_success_url(self):
        return reverse_lazy("player:player_list")


class PlayerCreate(PlayerCreateUpdateBaseView):
    """ Create player. """

    url_name = "player_create"
    url_reg = r"^player_create/$"
    action_name = "Add player"

    form_class = PlayerCreationForm

    def post(self, request):
        form = self.form_class(request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            context = {'form': form}
            return render(request, 'registration/player_create.html', context)

    def get(self, request):
        context = self.get_context_data()
        form = self.form_class
        context['form'] = form
        return render(request, 'registration/player_create.html', context)


class PlayerUpdate(PlayerCreateUpdateBaseView):
    """ Update player details. """

    pass


class PlayerDetail(View):
    """ Show player details. """

    pass


class PlayerList(ListView):
    """ List players. """

    url_name = "player_list"
    url_reg = r"^player_list/$"
    model = Player

    def get(self, request):
        context = dict()
        context['users'] = Player.objects.all()
        return render(request, 'player/player_list.html', context)
