<template>
  <div class="list">
    <h2 class='logo font-rem d-flex justify-center align-center' style='color: red; font-size: 6rem'>RMFlix</h2>
    <!-- <h3 class="text-h3">Personagens</h3> -->
    <vueper-slides
      class="no-shadow mt-8"
      :dragging-distance="70"
      :visible-slides="6"
      :bullets="false"
      :arrows="true"
      :slide-ratio="1 / 8"
      :gap="3"
      >
      <vueper-slide 
        :style="getBackground(character.image)" 
        :key="character.id" 
        class="bg-screen d-flex justify-center align-start font-rem" v-for="character in characters" 
        :title="character.name"
      />
    </vueper-slides>
  </div>
</template>

<script lang='ts'>
// eslint-disable-next-line @typescript-eslint/ban-ts-comment
// @ts-ignore: Unreachable code error
import { VueperSlides, VueperSlide } from 'vueperslides'
import { Component, Vue } from 'vue-property-decorator';
import { GraphQLService } from '@/services/graphql'
import { ICharacter } from '@/intefaces/characters'
import 'vueperslides/dist/vueperslides.css'

@Component({
  components: { VueperSlides, VueperSlide },
})
export default class Characters extends Vue {

  graphql = new GraphQLService()
  characters: ICharacter[] = []
  $refs: any

  async mounted(): Promise<void> {
    const query = `
      query {
        characters(page: 1) {
          info {
            count
          }
          results {
            id,
            name,
            image,
            location {
              name
            },
            episode {
              name
            }
          }
        }
      }
    `
    const response: any = await this.graphql.get(query)
    this.characters = response.data.data.characters.results
  }

  getBackground(image: string): string {
    return `background-image: url(${image})`
  }
}
</script>

<style lang="scss">
.logo {
  margin-top: 2vh;
}
.bg-screen {
  transition: all .5s;
  opacity: .3;
  &:hover {
    transform: scale(1.1);
    opacity: 1;
    width: 200px;
  }
}
</style> 
