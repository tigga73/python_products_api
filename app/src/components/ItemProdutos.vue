<script setup lang="ts">
import { Produto } from '@/types/Produto';

defineProps<{
  produto: Produto;
}>();
</script>

<template>
  <tr>
    <th>{{ produto.id }}</th>
    <td>{{ produto.nome }}</td>
    <td>{{ produto.marca }}</td>
    <td>{{ produto.preco }}</td>
    <td class="is-flex is-justify-content-center">
      <span class="icon">
        <i class="fas fa-trash"></i>
      </span>
    </td>
  </tr>
</template>

<style scoped lang="scss"></style>
