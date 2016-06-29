# Used 18min
class ListeningSongs:
    def listen(self, durations1, durations2, minutes, T):
        if len(durations1) < T or len(durations2) < T:
            return -1
        seconds = minutes * 60
        m_durations1 = sorted(durations1)
        m_durations2 = sorted(durations2)
        for i in range(T):
            seconds -= (m_durations1[i] + m_durations2[i])
        if seconds < 0:
            return -1
        all_durations = m_durations1[T:] + m_durations2[T:]
        all_durations = sorted(all_durations)
        count = 2 * T
        for i in range(len(all_durations)):
            if seconds - all_durations[i] < 0:
                return count
            else:
                count += 1
                seconds -= all_durations[i]
        return count

