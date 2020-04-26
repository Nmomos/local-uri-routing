<template>
  <v-container>
    <v-row class="text-center">
      <v-col cols="12">
        <v-img
          :src="require('../assets/logo.svg')"
          class="my-3"
          contain
          height="200"
        />
      </v-col>

      <v-col class="mb-4">
        <h1 class="display-2 font-weight-bold mb-3">
          Local ingress test
        </h1>
      </v-col>

      <v-col class="mb-5" cols="12">
        <h2 class="headline font-weight-bold mb-3">
          API Call
        </h2>
        <v-row justify="center">
          <v-btn class="mx-3" @click="getInfoA">
            <span class="mr-2">Calling A-API</span>
          </v-btn>

          <v-btn class="mx-3" @click="getInfoB">
            <span class="mr-2">Calling B-API</span>
          </v-btn>

          <v-btn class="mx-3" @click="getInfoC">
            <span class="mr-2">Calling C-API</span>
          </v-btn>
        </v-row>
      </v-col>

      <v-col class="mb-5" cols="12">
        <template v-if="infoResult.length">
          <h2 class="headline font-weight-bold mb-3">
            Results
          </h2>
          <p>
            {{ infoResult }}
          </p>
        </template>
        <p v-else>
          Please calling API
        </p>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from "axios";

export default {
  name: "HelloWorld",
  data: () => ({
    infoResult: [],
  }),
  methods: {
    getInfoA() {
      axios
        .get("http://localhost/api/a-api/")
        .then((response) => {
          response = response.data;
          this.infoResult = response;
        })
        .catch(() => {
          this.infoResult = [];
        });
    },
    getInfoB() {
      axios
        .get("http://localhost/api/b-api/")
        .then((response) => {
          response = response.data;
          this.infoResult = response;
        })
        .catch(() => {
          this.infoResult = [];
        });
    },
    getInfoC() {
      axios
        .get("http://localhost/api/c-api/")
        .then((response) => {
          response = response.data;
          this.infoResult = response;
        })
        .catch(() => {
          this.infoResult = [];
        });
    },
  },
};
</script>
