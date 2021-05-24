<template>
  <!--  size = 18-->
  <v-container>
    <v-card-title class="headline">
      Área do aluno
    </v-card-title>
    <input type="checkbox" id="checkbox" v-model="checked">
    <label for="checkbox">Comentário anônimo</label>
    <v-spacer></v-spacer>

    <v-row dense align="stretch">
      <!--      1ºbloco-->
      <v-col cols="12">
        <v-card>
          <v-card-text class="primary--text">
            <h5 class="text-truncate text-uppercase">CES777 - PROFESSOR ESPONGEBOB</h5>


            <v-spacer></v-spacer>

            <p>Professor:<v-text-field outlined v-model="professor_name" placeholder="Professor"></v-text-field></p>
            <p>Disciplina:<v-text-field outlined v-model="professor_subject" placeholder="Disciplina"></v-text-field></p>

            <p>Comentário:<v-text-field outlined v-model="message" placeholder="Deixe seu comentário sobre a eletiva"></v-text-field></p>
          </v-card-text>
          <v-btn
            color="primary"
          >
            ENVIAR
          </v-btn>
        </v-card>
      </v-col>
      </v-card-text>
      </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "comentario",
  head() {
    const title = "Comentário"
    return {
      title
    }
  },
}
</script>

<style scoped>

</style>
