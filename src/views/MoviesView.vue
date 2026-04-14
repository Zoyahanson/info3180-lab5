<template>
  <div class="container py-5">
    <h1 class="mb-4">Movies</h1>

    <div class="row row-cols-1 row-cols-md-3 g-4">
      <div v-for="movie in movies" :key="movie.id" class="col">
        
        <div class="card h-100 shadow-sm">
          <img :src="movie.poster" class="card-img-top" :alt="movie.title" />
          <div class="card-body">
            <h5 class="card-title">{{ movie.title }}</h5>
            <p class="card-text text-muted">
              {{ movie.description }}
            </p>
          </div>
        </div>
        </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";

let movies = ref([]);

function fetchMovies() {
  fetch("/api/v1/movies")
    .then(res => res.json())
    .then(data => {
        movies.value = data.movies;
    })
    .catch(err => console.error("Error fetching movies:", err));
}

onMounted(fetchMovies);
</script>

<style scoped>
.card-img-top {
  height: 400px;
  object-fit: cover;
}
</style>