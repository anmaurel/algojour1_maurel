export interface Bloc {
  index: number;
  hash: string;
  previous_hash: string;
  timestamp: string;
  data: string;
  nonce: number;
}

export type BlocChain = Bloc[];
