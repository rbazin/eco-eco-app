// Path: frontend\src\routes.js
import LoginPage from "./components/LoginPage.vue";
import RegisterPage from "./components/RegisterPage.vue";
import HomePage from "./components/HomePage.vue";
import FriendsPage from "./components/FriendsPage.vue";
import GuidePage from "./components/GuidePage.vue";
import ChartsPage from "./components/ChartsPage.vue";
import BadgePage from "./components/BadgePage.vue";
import ProfilePage from "./components/ProfilePage.vue";
import NotFound from "./components/NotFound";

export const routes = [
  { path: "/", component: LoginPage },
  { path: "/register", component: RegisterPage },
  { path: "/friends", component: FriendsPage },
  { path: "/guide", component: GuidePage },
  { path: "/badges", component: BadgePage },
  { path: "/charts", component: ChartsPage },
  { path: "/profile", component: ProfilePage },
  { path: "/home", component: HomePage },
  { path: "/:pathMatch(.*)*", component: NotFound } // default route for pages not found
];
