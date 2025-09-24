import { createApp } from 'vue'
import App from './App.vue'
import Home from './views/Home.vue';
import LoginAdmin from './views/LoginAdmin.vue';
import PanelAdmin from './components/PanelAdmin.vue';
import { createRouter, createWebHistory } from 'vue-router';

const routes = [
  { path: '/', component: Home },
  { path: '/admin', component: LoginAdmin },
  { path: '/paneladmin', component: PanelAdmin },
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

createApp(App).use(router).mount('#app');
