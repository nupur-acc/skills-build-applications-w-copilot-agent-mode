from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_user_creation(self):
        user = User.objects.create(name='Test User', email='test@example.com', team='Marvel')
        self.assertEqual(user.name, 'Test User')

class TeamModelTest(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='Marvel', members=['Iron Man', 'Spider-Man'])
        self.assertEqual(team.name, 'Marvel')

class ActivityModelTest(TestCase):
    def test_activity_creation(self):
        activity = Activity.objects.create(user='Iron Man', activity='Running', duration=30)
        self.assertEqual(activity.activity, 'Running')

class LeaderboardModelTest(TestCase):
    def test_leaderboard_creation(self):
        leaderboard = Leaderboard.objects.create(team='Marvel', points=100)
        self.assertEqual(leaderboard.team, 'Marvel')

class WorkoutModelTest(TestCase):
    def test_workout_creation(self):
        workout = Workout.objects.create(user='Spider-Man', workout='Push-ups', reps=50)
        self.assertEqual(workout.workout, 'Push-ups')
