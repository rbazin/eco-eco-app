// Path: frontend\src\routes.js
import LoginPage from "./components/LoginPage.vue";
import RegisterPage from "./components/RegisterPage.vue";
import HomePage from "./components/HomePage.vue";

export const routes = [
  { path: "/", component: LoginPage },
  { path: "/register", component: RegisterPage },
  { path: "/home", component: HomePage },
];
