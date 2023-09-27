from cosc343ChessQueens import ChessQueens
import random
import numpy as np

board = ChessQueens()

class agentFunction:

    def __init__(self):
        self.population = 1400
        self.chromosomes = self.create_chromosomes()
        self.evolved = self.evolve()

    def evolve(self):

        while True:

            c_max = 0
            cbest = None

            fitness = []
            # all methods for evolving
            for c in self.chromosomes:
                f = board.nonattacking_pairs(c)
                fitness.append(f)
                if f == 28:
                    board.show_state(c)
                    print("GAME COMPLETE: ", c)
                    return 1
                if f > c_max:
                    c_max = f
                    cbest = c

                total_sum = sum(fitness)
                newFitness = []

                for value in fitness:
                    newFitness.append(value / total_sum)

            print(cbest, c_max)
            board.show_state(cbest)


            newChildren = []
            for i in range(0,self.population):
                newParentsIndices = np.random.choice(len(self.chromosomes), size=2, replace=False, p=newFitness)
                newParent1 = self.chromosomes[newParentsIndices[0]]
                newParent2 = self.chromosomes[newParentsIndices[1]]
                child = self.cross_over(newParent1, newParent2)
                mutatedChild = self.mutate(child)
                newChildren.append(mutatedChild)

            self.chromosomes = newChildren




    def cross_over(self, parent1, parent2):
        uniform_crossover = [random.randint(0, 1) for _ in range(8)]
        newChild = []
        for i in range(len(parent1)):
            if uniform_crossover[i] == 1:
                newChild.append(parent1[i])
            else:
                newChild.append(parent2[i])

        npChild = np.array(newChild)
        if len(np.unique(npChild)) != 8:
            return self.cross_over(parent1, parent2)
        # print("new child: ", newChild)
        return newChild


    def mutate(self, child):
        mutateLevel = 0.11
        random_decimal = round(random.uniform(0, 1), 2)
        if random_decimal < mutateLevel:
            k = random.randint(0,7)
            v = random.randint(0,63)
            child[k] = v
        return child



    def create_chromosomes(self):
        num = self.population
        all_chromosomes = []
        for i in range(0, num):
            c = []
            for j in range(8):
                c.append(random.randint(0,63))
            all_chromosomes.append(c)
        # print(all_chromosomes)
        return all_chromosomes




if __name__ == '__main__':
    solver = agentFunction()