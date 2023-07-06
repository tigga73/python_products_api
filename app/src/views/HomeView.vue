<script setup lang="ts">
import ListaDeProdutos from '@/components/ListaDeProdutos.vue';
</script>

<template>
  <Suspense>
    <template #default>
      <ListaDeProdutos />
    </template>
    <template #fallback>
      <progress class="progress is-primary is-small" />
    </template>
  </Suspense>
</template>
