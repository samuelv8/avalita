<template>
  <v-container fluid>
    <v-card>
      <v-card-text class="primary--text">
        <v-row align="center" justify="center">
          <v-btn
            color="primary"
            text
            @click="reserve"
          >
            {{subject.code}} - {{subject.professor}}
          </v-btn>
        </v-row>
        <v-row align="center" justify="center">
          <v-rating
            :value="subject.grade"
            color="primary"
            dense
            half-increments
            readonly
            size="18"
          ></v-rating>
        </v-row>
        <v-row align="center" justify="center">{{subject.grade}}</v-row>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script>
export default {
  name: "AvaliacaoIndividual",
  data() {
    return {
      subject: {
        code: "CES-22",
        professor: "Karla",
        grade: "4",
      }
    }
  }
}
</script>

<style scoped>

</style>
