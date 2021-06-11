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
        <v-row>
          <v-col
            md="3"
          >
            <v-rating
              v-model="aval['pontualidade']"
              color="primary"
              background-color="primary"
              readonly
            ></v-rating>
            <div>
              <span>Pontualidade:</span>
              <span>{{aval['pontualidade']}}</span>
            </div>
          </v-col>
          <v-spacer/>
          <v-col
            md="3"
          >
            <v-rating
              v-model="aval['coerencia']"
              color="primary"
              background-color="primary"
              readonly
            ></v-rating>
            <div>
              <span>Coerência da correção:</span>
              <span>{{aval['coerencia']}}</span>
            </div>
          </v-col>
          <v-spacer/>
          <v-col
            md="3"
          >
            <v-rating
              v-model="aval['melacao']"
              color="primary"
              background-color="primary"
              readonly
            ></v-rating>
            <div>
              <span>Possibilidade de melação:</span>
              <span>{{aval['melacao']}}</span>
            </div>
          </v-col>
          <v-spacer/>
        </v-row>
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
      'pontualidade': Number,
      'coerencia': Number,
      'melacao': Number
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
