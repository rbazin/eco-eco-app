// Path: frontend\src\routes.js
import LoginPage from "./components/LoginPage.vue";
import RegisterPage from "./components/RegisterPage.vue";
import HomePage from "./components/HomePage.vue";
import FriendsPage from "./components/FriendsPage.vue";
import GuidePage from "./components/GuidePage.vue";
import ChartsPage from "./components/ChartsPage.vue";
import BadgePage from "./components/BadgePage.vue";
import ProfilePage from "./components/ProfilePage.vue";
import QuestionnairePage1 from "./components/QuestionnairePage1.vue";
import QuestionnairePage2 from "./components/QuestionnairePage2.vue";
import ChallengePage from "./components/ChallengePage.vue";

// Possible routes for the application
export const routes = [
  { path: "/", component: LoginPage },
  { path: "/register", component: RegisterPage },
  { path: "/questionnaire_1", component: QuestionnairePage1 },
  { path: "/questionnaire_2", component: QuestionnairePage2 },
  { path: "/friends", component: FriendsPage },
  { path: "/guide", component: GuidePage },
  { path: "/badges", component: BadgePage },
  { path: "/charts", component: ChartsPage },
  { path: "/profile", component: ProfilePage },
  { path: "/home", component: HomePage },
  { path: "/challenge", component: ChallengePage },
  { path: "/:pathMatch(.*)*", redirect: "/" }, // if the page is not found, redirect to the login page (improvement : send to 404 or home if logged in)
];
