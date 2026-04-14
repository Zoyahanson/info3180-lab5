<template>
  <div class="container mt-5">
    <div class="card p-4 shadow-sm mx-auto" style="max-width: 600px;">
      <h2 class="mb-4">Add New Movie</h2>

      <div v-if="successMessage" class="alert alert-success alert-dismissible fade show">
        {{ successMessage }}
      </div>

      <div v-if="errorMessages.length" class="alert alert-danger">
        <ul class="mb-0">
            <li v-for="(err, index) in errorMessages" :key="index">
                {{ err }}
            </li>
        </ul>
      </div>

      <form id="movieForm" @submit.prevent="saveMovie">
        <div class="mb-3">
          <label class="form-label fw-bold">Movie Title</label>
          <input type="text" name="title" class="form-control" placeholder="Enter title" />
        </div>

        <div class="mb-3">
          <label class="form-label fw-bold">Description</label>
          <textarea name="description" class="form-control" rows="4" placeholder="Enter description"></textarea>
        </div>

        <div class="mb-3">
          <label class="form-label fw-bold">Movie Poster</label>
          <input type="file" name="poster" class="form-control" />
        </div>

        <button type="submit" class="btn btn-primary w-100 py-2 mt-2">Submit Movie</button>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";

let csrf_token = ref("");

let successMessage = ref("");
let errorMessages = ref([]);

function getCsrfToken() {
  fetch("/api/v1/csrf-token")
    .then(res => res.json())
    .then(data => {
      csrf_token.value = data.csrf_token;
    });
}

function saveMovie() {
  let movieForm = document.getElementById("movieForm");
  let form_data = new FormData(movieForm);

  successMessage.value = "";
  errorMessages.value = [];

  fetch("/api/v1/movies", {
    method: "POST",
    body: form_data,
    headers: {
      'X-CSRFToken': csrf_token.value
    }
  })
    .then(async res => {
      const data = await res.json();

      if (res.ok) {
        successMessage.value = data.message || "Movie uploaded successfully!";
        errorMessages.value = [];
        movieForm.reset();
      } else {
        successMessage.value = "";
        if (data.errors && Array.isArray(data.errors)) {
            errorMessages.value = data.errors;
        } else {
            errorMessages.value = ["Upload failed"];
        }
      }
    })
    .catch((error) => {
        console.error("Fetch Error:", error);
        successMessage.value = "";
        errorMessages.value = ["Server error. Please try again."];
    }); 
    }

onMounted(() => {
  getCsrfToken();
});
</script>

