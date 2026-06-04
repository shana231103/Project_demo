<template>
  <div class="w-full overflow-x-auto rounded-2xl border border-ink-700">

    <!-- Table header -->
    <table class="w-full text-sm">
      <thead>
        <tr class="border-b border-ink-700">
          <th class="text-left px-5 py-4 font-display font-semibold text-xs uppercase
                     tracking-widest text-ink-600 w-8">#</th>
          <th class="text-left px-5 py-4 font-display font-semibold text-xs uppercase
                     tracking-widest text-ink-600">Người chơi</th>
          <th class="text-left px-5 py-4 font-display font-semibold text-xs uppercase
                     tracking-widest text-ink-600">Đội</th>
          <th class="text-right px-5 py-4 font-display font-semibold text-xs uppercase
                     tracking-widest text-ink-600">KDA</th>
          <th class="text-center px-5 py-4 font-display font-semibold text-xs uppercase
                     tracking-widest text-ink-600">Tier</th>
        </tr>
      </thead>

      <tbody>
        <!-- Skeleton rows -->
        <template v-if="loading">
          <tr v-for="i in 6" :key="`sk-${i}`"
              class="border-b border-ink-800/60">
            <td class="px-5 py-4" colspan="5">
              <div class="h-5 rounded-md bg-gradient-to-r from-ink-800 via-ink-700 to-ink-800
                          bg-[length:200%_100%] animate-shimmer" />
            </td>
          </tr>
        </template>

        <!-- Empty state -->
        <tr v-else-if="players.length === 0">
          <td colspan="5" class="px-5 py-16 text-center">
            <p class="text-4xl mb-3">🔍</p>
            <p class="text-ink-600 font-body">Không tìm thấy người chơi nào.</p>
          </td>
        </tr>

        <!-- Data rows -->
        <template v-else>
          <tr
            v-for="(player, idx) in players"
            :key="player.name"
            class="border-b border-ink-800/60 hover:bg-ink-800/50 transition-colors duration-150
                   group cursor-default"
            :style="{ animationDelay: `${idx * 40}ms` }"
            :class="idx < 8 ? `animate-slide-up-${Math.min(idx + 1, 4)}` : 'animate-fade-in'"
          >
            <!-- Rank -->
            <td class="px-5 py-4 font-mono text-xs text-ink-600">
              {{ String(idx + 1).padStart(2, "0") }}
            </td>

            <!-- Name -->
            <td class="px-5 py-4">
              <div class="flex items-center gap-3">
                <!-- Avatar initials -->
                <div
                  class="w-8 h-8 rounded-lg flex items-center justify-center shrink-0
                         font-display font-bold text-xs text-ink-950 select-none"
                  :style="{ background: avatarColor(player.name) }"
                >
                  {{ initials(player.name) }}
                </div>
                <span class="font-body font-medium text-white">{{ player.name }}</span>
              </div>
            </td>

            <!-- Team -->
            <td class="px-5 py-4">
              <span class="font-body text-ink-500 text-xs bg-ink-800 px-2 py-1 rounded-lg
                           border border-ink-700">
                {{ player.team }}
              </span>
            </td>

            <!-- KDA -->
            <td class="px-5 py-4 text-right">
              <span
                class="font-mono font-semibold"
                :class="kdaColor(player.kda)"
              >
                {{ player.kda.toFixed(2) }}
              </span>
            </td>

            <!-- Tier -->
            <td class="px-5 py-4 text-center">
              <TierBadge :tier="player.performance_tier ?? 'Bronze'" />
            </td>
          </tr>
        </template>
      </tbody>
    </table>

    <!-- Footer count -->
    <div v-if="!loading && players.length > 0"
         class="px-5 py-3 border-t border-ink-800 flex justify-between items-center">
      <span class="text-xs text-ink-600 font-body">
        {{ players.length }} người chơi
      </span>
      <span class="text-xs text-ink-600 font-mono">
        avg KDA:
        <span class="text-acid font-semibold">{{ avgKda }}</span>
      </span>
    </div>
  </div>
</template>

<script setup>
import { computed } from "vue";
import TierBadge from "./TierBadge.vue";

const props = defineProps({
  players: { type: Array, default: () => [] },
  loading: { type: Boolean, default: false },
});

function initials(name) {
  return name.slice(0, 2).toUpperCase();
}

function avatarColor(name) {
  const colors = [
    "#c8f53b", "#a0c8ff", "#ff4d2b", "#f0c030",
    "#80e0c0", "#d090f0", "#f080a0",
  ];
  let h = 0;
  for (let i = 0; i < name.length; i++) h = (h * 31 + name.charCodeAt(i)) & 0xffffffff;
  return colors[Math.abs(h) % colors.length];
}

function kdaColor(kda) {
  if (kda >= 5) return "text-amber-300";
  if (kda >= 3) return "text-acid";
  if (kda >= 2) return "text-white";
  return "text-ink-500";
}

const avgKda = computed(() => {
  if (!props.players.length) return "0.00";
  const sum = props.players.reduce((a, p) => a + p.kda, 0);
  return (sum / props.players.length).toFixed(2);
});
</script>
