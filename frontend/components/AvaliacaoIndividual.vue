<template>
  <v-container fluid>
    <v-card>
      <v-card-text class="primary--text">
        <v-row align="center" justify="center">
<!--          <v-btn-->
<!--            color="primary"-->
<!--            text-->
<!--            @click="reserve"-->
<!--          >-->
<!--            {{aval['subj_name']}} - {{aval['professor']}}-->
<!--          </v-btn>-->
          <v-card-text>
            {{aval['subj_name']}} - {{aval['professor']}}
          </v-card-text>
        </v-row>
        <v-row align="center" justify="center">
          <v-rating
            :value="aval.grade"
            color="primary"
            dense
            half-increments
            readonly
            size="18"
          ></v-rating>
        </v-row>
        <v-row align="center" justify="center">{{aval['grade']}}</v-row>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script>
export default {
  name: "AvaliacaoIndividual",
  props: {
    aval: {
      'subj_name': String,
      'professor': String,
      'grade': Number,
    },
  },
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
