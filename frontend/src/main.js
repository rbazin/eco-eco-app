import { createApp } from "vue";
import App from "./App.vue";

// Enable the use of icons in the app
import FontAwesomeIcon from "./fontawesome-icons.js";

// Enable the use of stores in the app
import { createPinia } from "pinia";

const pinia = createPinia();

// Enable the use of router in the app
import { createRouter, createWebHistory } from "vue-router";
import { routes } from "./routes";

const router = createRouter({
  history: createWebHistory(),
  routes,
});

const app = createApp(App);

app.component("font-awesome-icon", FontAwesomeIcon);
app.use(router);
app.use(pinia);

app.mount("#app");
