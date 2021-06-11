<template>
  <!--  size = 18-->
  <v-container>
    <v-card-title class="headline">
      Área do aluno
    </v-card-title>

<!--    <v-btn-->
<!--      color="primary"-->
<!--      nuxt-->
<!--      to="/comentario"-->
<!--    >-->
<!--      + adicione seu comentário-->
<!--    </v-btn>-->

    <v-row dense align="stretch">
      <!--      1ºbloco-->
      <v-col cols="15">
        <v-card>
          <v-card-text class="primary--text">
            <h5 class="text-truncate text-uppercase">CES777 - PROFESSOR ESPONGEBOB</h5>
            <!--            <h1>{{ sales }}</h1>-->
            <p>Pontualidade</p>

            <v-rating
              align="center"
              :value="4.5"
              color="primary"
              dense
              half-increments
              readonly
              size="18"
            ></v-rating>
            <div align="center" class="grey--text ms-4">4.5</div>

            <p>Coerência da cobrança</p>
            <v-rating
              align="center"
              :value="3.5"
              color="primary"
              dense
              half-increments
              readonly
              size="18"
            ></v-rating>
            <div align="center" class="grey--text ms-4">4.5</div>

            <p>Possibilidade de melação</p>
            <v-rating
              align="center"
              :value="2.0"
              color="primary"
              dense
              half-increments
              readonly
              size="18"
            ></v-rating>
            <div align="center" class="grey--text ms-4">4.5</div>
          </v-card-text>
          <v-card-text class="primary--text">

            <v-spacer></v-spacer>

            <!--            <p>Professor:<v-text-field outlined v-model="professor_name" placeholder="Professor"></v-text-field></p>-->
            <!--            <p>Disciplina:<v-text-field outlined v-model="professor_subject" placeholder="Disciplina"></v-text-field></p>-->

            <p>Comentário:<v-text-field outlined v-model="message" placeholder="Deixe seu comentário sobre a eletiva"></v-text-field></p>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "avaliacao",
  head() {
    const title = "Avaliação"
    return {
      title
    }
  },
}
</script>

<style scoped>

</style>
