import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '../views/HomeView.vue';
import NovoProdutoView from '../views/NovoProdutoView.vue';

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/NovoProduto',
      name: 'NovoProduto',
      component: NovoProdutoView,
    },
  ],
});

export default router;
