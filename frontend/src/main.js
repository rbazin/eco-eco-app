import { createApp } from "vue";
import App from "./App.vue";

import { createPinia } from "pinia";

const pinia = createPinia();

import { createRouter, createWebHistory } from "vue-router";
import { routes } from "./routes";

const router = createRouter({
  history: createWebHistory(),
  routes,
});

const app = createApp(App);

app.use(router);
app.use(pinia);

app.mount("#app");
