<template>
  <v-card
    class="mx-auto"
    max-width="1500"
  >
    <v-container fluid>
      <v-row dense>
        <v-col
          v-for="card in cards"
          :key="card.title"
          :cols="card.flex"
        >
          <v-card
            nuxt
            to="/departamentos/comp"
          >
            <v-img
              :src="card.src"
              class="white--text text-center align-center"
              gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
              height="170px"
            >
              <v-card-text class="headline text_dpto">{{ card.title }}</v-card-text>
            </v-img>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </v-card>
</template>

<script>
export default {
  data: () => ({
    cards: [
      {
        title: 'Fundamental',
        src: 'http://www.ita.br/sites/default/files/styles/noticia_interno/public/pictures/noticias/capa_12.jpg?itok=-Z47J-6E',
        flex: 6
      },
      {title: 'Computação', src: 'http://www.comp.ita.br/assets/images/PredioComp.jpg', flex: 6},
      {title: 'Civil', src: 'https://cdn.vuetifyjs.com/images/cards/road.jpg', flex: 6},
      {title: 'Aeronáutica e Aeroespacial', src: 'https://cdn.vuetifyjs.com/images/cards/plane.jpg', flex: 6},
      {
        title: 'Mecânica',
        src: 'http://www.ita.br/sites/default/files/styles/large/public/eb5ecd6a8cc26d68893449708fa21d45.png?itok=Tw9TR-3Z',
        flex: 6
      },
      {
        title: 'Eletrônica',
        src: 'http://www.ita.br/sites/default/files/styles/large/public/154653fff2e47c02182024d179905430.jpg?itok=6xRhfgrg',
        flex: 6
      },
    ],
  }),
  name: "kanban-departamentos"
}
</script>

<style scoped>
.text_dpto {
  text-transform: uppercase;
}
</style>
