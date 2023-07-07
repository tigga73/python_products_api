import { NovoProduto, Produto } from '@/types/Produto';
import { defineStore } from 'pinia';
import { ref } from 'vue';

export const useProdutoStore = defineStore('produtos', () => {
  const produtos = ref<Produto[]>([]);

  async function obterProdutos(): Promise<void> {
    const res = await window.fetch('http://127.0.0.1:5000/produtos');
    const data = (await res.json()) as Produto[];

    produtos.value = data;
  }

  async function deletarProduto(id: string): Promise<void> {
    await window.fetch(`http://127.0.0.1:5000/produto/${id}`, {
      method: 'DELETE',
    });
  }

  async function criarProduto(novoProduto: NovoProduto): Promise<void> {
    const body = JSON.stringify(novoProduto);
    await window.fetch('http://127.0.0.1:5000/produtos', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body,
    });
  }

  return { produtos, obterProdutos, criarProduto, deletarProduto };
});
