<script setup lang="ts">
import { useProdutoStore } from '@/stores/produtoStore';
import ItemProdutos from './ItemProdutos.vue';
import { storeToRefs } from 'pinia';
import { Produto } from '@/types/Produto';
import { onMounted } from 'vue';

const produtoStore = useProdutoStore();

const { produtos } = storeToRefs(produtoStore);

async function handleDeletarProduto(id: string) {
  await produtoStore.deletarProduto(id);
  await produtoStore.obterProdutos();
}

onMounted(async () => {
  await produtoStore.obterProdutos();
});
</script>

<template>
  <div class="title">
    <h1 class="title has-text-centered">Todos os Produtos</h1>
  </div>
  <table class="table is-striped is-fullwidth">
    <thead>
      <tr>
        <th>Id</th>
        <th>Nome</th>
        <th>Marca</th>
        <th>Preço</th>
        <th class="has-text-centered">Ações</th>
      </tr>
    </thead>
    <tbody>
      <ItemProdutos
        v-for="produto in produtos"
        :key="produto.id"
        :produto="produto"
        @deletar-produto="handleDeletarProduto"
      />
    </tbody>
  </table>
  <RouterLink to="/NovoProduto" class="button is-link">
    Adicionar Produto
  </RouterLink>
</template>

<style scoped></style>
