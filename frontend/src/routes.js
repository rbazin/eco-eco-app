// Path: frontend\src\routes.js
import LoginPage from "./components/LoginPage.vue";
import RegisterPage from "./components/RegisterPage.vue";
import HomePage from "./components/HomePage.vue";
import FriendsPage from "./components/FriendsPage.vue";
import ChartsPage from "./components/ChartsPage.vue";
import BadgePage from "./components/BadgePage.vue";
import ProfilePage from "./components/ProfilePage.vue";
import QuestionnairePage1 from "./components/QuestionnairePage1.vue";
import QuestionnairePage2 from "./components/QuestionnairePage2.vue";
import ChallengePage from "./components/ChallengePage.vue";
import AllChallenges from "./components/AllChallengesPage.vue";
import SelectChallenge from "./components/SelectChallenge.vue";
import TutorialPage from "./components/TutorialPage.vue";
import HelpPage from "./components/HelpPage.vue";
import AddFriendPage from "@/components/AddFriendPage";
import FriendProfilePage from "@/components/FriendProfilePage.vue";

// Possible routes for the application
export const routes = [
  { path: "/", component: LoginPage },
  { path: "/help", component: HelpPage },
  { path: "/register", component: RegisterPage },
  { path: "/questionnaire_1", component: QuestionnairePage1 },
  { path: "/questionnaire_2", component: QuestionnairePage2 },
  { path: "/friends", component: FriendsPage },
  { path: "/add-friend", component: AddFriendPage },
  { path: "/badges", component: BadgePage },
  { path: "/charts", component: ChartsPage },
  { path: "/profile", component: ProfilePage },
  { path: "/home", component: HomePage },
  { path: "/challenge", component: ChallengePage },
  { path: "/all-challenges", component: AllChallenges },
  { path: "/tutorial", component: TutorialPage },
  {
    path: "/select-challenge/:id",
    name: "SelectChallenge",
    component: SelectChallenge,
  },
  {
    path: "/friend-profile/:id",
    name: "FriendProfilePage",
    component: FriendProfilePage,
  },
  { path: "/:pathMatch(.*)*", redirect: "/" }, // if the page is not found, redirect to the login page (improvement : send to 404 or home if logged in)
];
