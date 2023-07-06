<script setup lang="ts">
import { useProdutoStore } from '@/stores/produtoStore';
import ItemProdutos from './ItemProdutos.vue';
import { storeToRefs } from 'pinia';

const produtoStore = useProdutoStore();
await produtoStore.fetchProdutos();

const { produtos } = storeToRefs(produtoStore);
</script>

<template>
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
      />
    </tbody>
  </table>
</template>

<style scoped lang="scss"></style>
