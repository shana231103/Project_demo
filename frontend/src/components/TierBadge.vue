<template>
  <span
    class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-xs font-display
           font-semibold tracking-wide uppercase"
    :class="styles[tier] ?? styles.Bronze"
  >
    <span>{{ icon[tier] ?? '🥉' }}</span>
    {{ tier }}
  </span>
</template>

<script setup>
defineProps({
  tier: { type: String, default: "Bronze" },
});

const styles = {
  Legend: "bg-amber-400/15 text-amber-300 ring-1 ring-amber-400/30",
  Diamond: "bg-frost/15 text-frost ring-1 ring-frost/30",
  Gold: "bg-yellow-500/15 text-yellow-400 ring-1 ring-yellow-500/30",
  Bronze: "bg-orange-900/30 text-orange-400 ring-1 ring-orange-700/30",
};

const icon = {
  Legend: "👑",
  Diamond: "💎",
  Gold: "⭐",
  Bronze: "🥉",
};
</script>
