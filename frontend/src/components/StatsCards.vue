<template>
  <div class="grid grid-cols-2 sm:grid-cols-4 gap-3">
    <div
      v-for="(card, i) in cards"
      :key="card.label"
      class="rounded-xl border border-ink-700 bg-ink-800/60 px-4 py-4
             flex flex-col gap-1 animate-slide-up"
      :style="{ animationDelay: `${i * 60}ms` }"
    >
      <span class="text-xs font-display uppercase tracking-widest text-ink-600">
        {{ card.label }}
      </span>
      <span class="text-2xl font-display font-bold" :class="card.color">
        {{ card.value }}
      </span>
    </div>
  </div>
</template>

<script setup>
import { computed } from "vue";

const props = defineProps({
  players: { type: Array, default: () => [] },
});

const cards = computed(() => {
  const p = props.players;
  if (!p.length) return [
    { label: "Tổng", value: "—", color: "text-white" },
    { label: "KDA TB", value: "—", color: "text-acid" },
    { label: "KDA Cao", value: "—", color: "text-amber-300" },
    { label: "Legend", value: "—", color: "text-frost" },
  ];

  const avg = p.reduce((a, x) => a + x.kda, 0) / p.length;
  const max = Math.max(...p.map((x) => x.kda));
  const legends = p.filter((x) => (x.performance_tier ?? "") === "Legend").length;

  return [
    { label: "Tổng", value: p.length, color: "text-white" },
    { label: "KDA TB", value: avg.toFixed(2), color: "text-acid" },
    { label: "KDA Cao", value: max.toFixed(2), color: "text-amber-300" },
    { label: "Legend", value: legends, color: "text-frost" },
  ];
});
</script>
