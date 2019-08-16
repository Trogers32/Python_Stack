from django.shortcuts import render, redirect
from .models import League, Team, Player
from django.db.models import Q, Count

from . import team_maker

def index(request):
	context = {
		"asc_teams" : Team.objects.filter(league__name="Atlantic Soccer Conference"),
		"bp_players" : Player.objects.filter(curr_team__team_name="Penguins", curr_team__location="Boston"),
		"icbc_players" : Player.objects.filter(curr_team__league__name="International Collegiate Baseball Conference"),
		"acaf_players" : Player.objects.filter(last_name="Lopez",
			curr_team__league__name="American Conference of Amateur Football"),
		"fb_players" : Player.objects.filter(curr_team__league__sport="Football"),
		"sophias" : Player.objects.filter(first_name="Sophia"),
		"flores" : Player.objects.filter(Q(last_name="Flores"), ~Q(curr_team__team_name="Roughriders",curr_team__location="Washington")),
		"sEvans" : Player.objects.get(first_name="Samuel", last_name="Evans").all_teams.all(),
		"mtc_players" : Team.objects.get(location="Manitoba", team_name="Tiger-Cats").all_players.all(),
		"wv_former" : Team.objects.get(team_name="Vikings", location="Wichita").all_players.exclude(curr_team__team_name="Vikings"),
		"jgray" : Player.objects.get(first_name="Jacob", last_name="Gray").all_teams.exclude(team_name="Colts"),
		"joshs" : Player.objects.filter(first_name="Joshua", all_teams__league__name="Atlantic Federation of Amateur Baseball Players"),
		"annotate" : Team.objects.annotate(Count('all_players')).filter(all_players__count__gte=12),
		"pct" : Player.objects.annotate(num_teams=Count('all_teams')).order_by('-num_teams'),
		
		"leagues": League.objects.all(),
		"teams": Team.objects.all(),
		"players": Player.objects.all(),
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")

		# "baseball_leagues": League.objects.filter(sport="Baseball"),
		# "womens_leagues" : League.objects.filter(name__contains="women"),
		# "hockey_leagues" : League.objects.filter(name__contains="hockey"),
		# "not_football_leagues" : League.objects.exclude(name__contains="football"),
		# "conference_leagues" : League.objects.filter(name__contains="conference"),
		# "atlantic_leagues" : League.objects.filter(name__contains="atlantic"),
		# "dallas_teams" : League.objects.filter(teams__location="Dallas"),
		# "raptors_teams" : Team.objects.filter(team_name__contains="raptors"),
		# "city_teams" : Team.objects.filter(location__contains="city"),
		# "T_teams" : Team.objects.filter(team_name__startswith="t"),
		# "alph_teams" : Team.objects.all().order_by('location'),
		# "revalph_teams" : Team.objects.all().order_by('-team_name'),
		# "coopers" : Player.objects.filter(last_name="Cooper"),
		# "joshuas" : Player.objects.filter(first_name="Joshua"),
		# "no_josh" : Player.objects.filter(last_name="Cooper").exclude(first_name="Joshua"),
		# "alexs" : Player.objects.filter(Q(first_name="Alexander") | Q(first_name="Wyatt")),