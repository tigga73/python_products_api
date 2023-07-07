<script setup lang="ts">
import { Produto } from '@/types/Produto';

const props = defineProps<{
  produto: Produto;
}>();

const emit = defineEmits<{
  (event: 'deletarProduto', idProduto: string): void;
}>();

function handleClick() {
  emit('deletarProduto', props.produto.id);
}
</script>

<template>
  <tr>
    <th>{{ produto.id }}</th>
    <td>{{ produto.nome }}</td>
    <td>{{ produto.marca }}</td>
    <td>{{ produto.preco }}</td>
    <td class="is-flex is-justify-content-center">
      <span class="icon" @click="handleClick">
        <i class="fas fa-trash"></i>
      </span>
    </td>
  </tr>
</template>

<style scoped>
span.icon:hover {
  cursor: pointer;
}
</style>
