// Path: frontend\src\routes.js
import WelcomePage from "./components/WelcomePage.vue";
import LoginPage from "./components/LoginPage.vue";
import RegisterPage from "./components/RegisterPage.vue";

export const routes = [
  { path: "/", component: WelcomePage },
  { path: "/login", component: LoginPage },
  { path: "/register", component: RegisterPage },
];
