<template>
  <div class="grid grid-cols-1 sm:grid-cols-3 gap-4">
    <div
      v-for="(card, i) in cards"
      :key="card.label"
      class="rounded-xl border border-slate-200 bg-white px-5 py-4
             flex flex-col gap-1 shadow-sm hover:shadow transition-shadow duration-200 animate-slide-up"
      :style="{ animationDelay: `${i * 60}ms` }"
    >
      <span class="text-xs uppercase tracking-widest text-black font-mono">
        {{ card.label }}
      </span>
      <span class="text-2xl font-bold" :class="card.color">
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
    { label: "Total Players", value: "—", color: "text-slate-800" },
    { label: "Average KDA", value: "—", color: "text-blue-600" },
    { label: "Max KDA", value: "—", color: "text-amber-600" },
  ];

  const avg = p.reduce((a, x) => a + x.kda, 0) / p.length;
  const max = Math.max(...p.map((x) => x.kda));

  return [
    { label: "Total Players", value: p.length, color: "text-slate-800" },
    { label: "Average KDA", value: avg.toFixed(2), color: "text-blue-600" },
    { label: "Max KDA", value: max.toFixed(2), color: "text-amber-600" },
  ];
});
</script>
