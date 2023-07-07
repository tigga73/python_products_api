export interface NovoProduto {
  nome: string;
  marca: string;
  preco: number;
}

export interface Produto extends NovoProduto {
  id: string;
}
