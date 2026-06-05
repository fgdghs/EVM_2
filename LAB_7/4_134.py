class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # Если суммарный расход превышает суммарный запас газа, круг невозможен
        if sum(gas) < sum(cost):
            return -1

        total_tank = 0
        start_index = 0

        for i in range(len(gas)):
            # Добавляем разницу между газом на станции и затратами на путь дальше
            total_tank += gas[i] - cost[i]

            # Если бак стал отрицательным, значит текущий старт не подходит
            if total_tank < 0:
                # Назначаем следующую станцию новой точкой старта
                start_index = i + 1
                # Сбрасываем бак для нового старта
                total_tank = 0

        return start_index