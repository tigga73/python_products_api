<script setup lang="ts">
import { useProdutoStore } from '@/stores/produtoStore';
import { NovoProduto } from '@/types/Produto';
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const nome = ref('');
const marca = ref('');
const preco = ref<number | null>(null);

const produtoStore = useProdutoStore();
const router = useRouter();

async function handleSubmit() {
  const novoProduto: NovoProduto = {
    nome: nome.value,
    marca: marca.value,
    preco: preco.value as number,
  };

  await produtoStore.criarProduto(novoProduto);
  router.push({ path: '/' });
}
</script>

<template>
  <div class="title">
    <h1 class="title has-text-centered">Adicionar Produto</h1>
  </div>
  <form @submit.prevent="handleSubmit">
    <div class="field">
      <label class="label">Nome</label>
      <div class="control">
        <input
          v-model="nome"
          class="input"
          name="Nome"
          type="text"
          placeholder="Placa de Vídeo RX 6600 CLD 8G"
        />
      </div>
    </div>

    <div class="field">
      <label class="label">Marca</label>
      <div class="control">
        <input
          v-model="marca"
          name="Marca"
          class="input"
          type="text"
          placeholder="AMD"
        />
      </div>
    </div>

    <div class="field">
      <label class="label">Preço</label>
      <div class="control">
        <input
          v-model="preco"
          name="Preço"
          class="input"
          type="number"
          placeholder="699.90"
          step="0.01"
        />
      </div>
    </div>

    <div class="buttons">
      <RouterLink to="/" class="button is-danger">Cancelar</RouterLink>
      <button class="button is-primary" type="submit">Adicionar Produto</button>
    </div>
  </form>
</template>

<style scoped></style>
