<template>
  <v-container>
    <v-card>
      <v-card-title>
        Avaliação
      </v-card-title>

      <v-row>
        <v-col
          md="6"
          offset-md="3"
        >
          <v-text-field
            v-model="aval.subject"
            label="Disciplina"
            required
          ></v-text-field>
        </v-col>
      </v-row>

      <v-row>
        <v-col
          md="6"
          offset-md="3"
        >
          <v-text-field
            v-model="aval.professor"
            label="Professor"
            required
          ></v-text-field>
        </v-col>
      </v-row>

      <v-row>
        <v-col
          md="4"
        >
          <v-rating
            v-model="aval.pontualidade"
            large
          ></v-rating>
          <div>
            <span>Pontualidade:</span>
            <span>{{aval.pontualidade}}</span>
          </div>
        </v-col>

        <v-col
          md="4"
        >
          <v-rating
            v-model="aval.coerencia"
            large
          ></v-rating>
          <div>
            <span>Coerência da correção:</span>
            <span>{{aval.coerencia}}</span>
          </div>
        </v-col>

        <v-col
          md="4"
        >
          <v-rating
            v-model="aval.melacao"
            large
          ></v-rating>
          <div>
            <span>Possibilidade de melação:</span>
            <span>{{aval.melacao}}</span>
          </div>
        </v-col>
      </v-row>

      <v-row>
        <v-col
          md="6"
          offset-md="3"
        >
          <p>Comentário:
            <v-text-field
              outlined
              v-model="aval.comment"
              label="Deixe seu comentário sobre a matéria"
            ></v-text-field>
          </p>
        </v-col>
      </v-row>
    </v-card>
  </v-container>
</template>

<script>
export default {
  name: "AdicionarAvaliacao",
  data: () => ({
    overlay: false,
    aval: {
      subject: '',
      professor: '',
      pontualidade: 0,
      coerencia: 0,
      melacao: 0,
      comment: ''
    }
  })
}
</script>

<style scoped>

</style>
