import { createApp } from 'vue';
import { createPinia } from 'pinia';

import App from './App.vue';
import router from './router';
import { useProdutoStore } from './stores/produtoStore';

const app = createApp(App);

app.use(createPinia());
app.use(router);

app.mount('#app');

// const produtoStore = useProdutoStore();

// Promise.all([produtoStore.fetchProdutos()]).then(() => {
//   app.use(router);
//   app.mount('#app');
// });
