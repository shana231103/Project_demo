<template>
  <div class="relative w-full max-w-lg">
    <!-- Input wrapper -->
    <div
      class="flex items-center gap-3 px-4 py-3 rounded-xl border transition-all duration-200"
      :class="focused
        ? 'border-acid bg-ink-800 shadow-[0_0_0_3px_rgba(200,245,59,0.12)]'
        : 'border-ink-600 bg-ink-800 hover:border-ink-500'"
    >
      <!-- Search icon -->
      <svg
        class="w-4 h-4 shrink-0 transition-colors duration-200"
        :class="focused ? 'text-acid' : 'text-ink-600'"
        viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="2"
      >
        <circle cx="9" cy="9" r="6" />
        <path d="M15 15l3 3" stroke-linecap="round" />
      </svg>

      <!-- Input -->
      <input
        v-model="query"
        type="text"
        placeholder="Tìm kiếm tên người chơi…"
        class="flex-1 bg-transparent text-sm font-body text-white placeholder-ink-600
               outline-none caret-acid"
        @focus="focused = true"
        @blur="focused = false"
        @keydown.enter="emit('search', query)"
        @keydown.escape="clear"
      />

      <!-- Clear button -->
      <button
        v-if="query"
        @click="clear"
        class="shrink-0 w-5 h-5 rounded-full bg-ink-600 hover:bg-ink-500 flex items-center
               justify-center transition-colors duration-150"
      >
        <svg viewBox="0 0 12 12" class="w-2.5 h-2.5 text-white" fill="none"
             stroke="currentColor" stroke-width="2" stroke-linecap="round">
          <path d="M2 2l8 8M10 2l-8 8" />
        </svg>
      </button>
    </div>

    <!-- Hint -->
    <p class="mt-1.5 text-xs text-ink-600 font-body pl-1">
      Nhấn <kbd class="px-1 py-0.5 rounded bg-ink-700 text-ink-500 font-mono text-[10px]">Enter</kbd>
      để tìm kiếm
    </p>
  </div>
</template>

<script setup>
import { ref, watch } from "vue";

const props = defineProps({
  modelValue: { type: String, default: "" },
});
const emit = defineEmits(["update:modelValue", "search", "clear"]);

const query = ref(props.modelValue);
const focused = ref(false);

watch(query, (val) => emit("update:modelValue", val));
watch(() => props.modelValue, (val) => { query.value = val; });

function clear() {
  query.value = "";
  emit("clear");
}
</script>
