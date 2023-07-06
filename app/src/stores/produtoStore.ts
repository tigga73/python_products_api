import { Produto } from '@/types/Produto';
import { defineStore } from 'pinia';
import { ref } from 'vue';

export const useProdutoStore = defineStore('produtos', () => {
  const produtos = ref<Produto[]>([]);

  async function fetchProdutos(): Promise<void> {
    const res = await window.fetch('http://127.0.0.1:5000/produtos');
    const data = (await res.json()) as Produto[];

    produtos.value = data;
  }

  return { produtos, fetchProdutos };
});
