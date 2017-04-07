import scipy.interpolate
import scipy.optimize

from uncertainpy.features import GeneralSpikingFeatures

class SpikingFeatures(GeneralSpikingFeatures):
    def nrSpikes(self, t, U):
        return None, self.spikes.nr_spikes


    def time_before_first_spike(self, t, U):
        if self.spikes.nr_spikes <= 0:
            return None, None

        return None, self.spikes.spikes[0].t_spike


    def spike_rate(self, t, U):
        if self.spikes.nr_spikes < 0:
            return None, None

        return None, self.spikes.nr_spikes/float(self.t[-1] - self.t[0])


    def average_AP_overshoot(self, t, U):
        if self.spikes.nr_spikes <= 0:
            return None, None

        sum_AP_overshoot = 0
        for spike in self.spikes:
            sum_AP_overshoot += spike.U_spike
        return None, sum_AP_overshoot/float(self.spikes.nr_spikes)


    def average_AHP_depth(self, t, U):
        if self.spikes.nr_spikes <= 0:
            return None, None

        sum_AHP_depth = 0
        for i in range(self.spikes.nr_spikes - 1):
            sum_AHP_depth += min(self.U[self.spikes[i].global_index:self.spikes[i+1].global_index])

        return None, sum_AHP_depth/float(self.spikes.nr_spikes)


    def average_AP_width(self, t, U):
        if self.spikes.nr_spikes <= 0:
            return None, None

        sum_AP_width = 0
        for spike in self.spikes:
            U_width = (spike.U_spike + spike.U[0])/2.

            U_interpolation = scipy.interpolate.interp1d(spike.t, spike.U - U_width)

            # root1 = scipy.optimize.fsolve(U_interpolation, (spike.t_spike - spike.t[0])/2. + spike.t[0])
            # root2 = scipy.optimize.fsolve(U_interpolation, (spike.t[-1] - spike.t_spike)/2. + spike.t_spike)

            root1 = scipy.optimize.brentq(U_interpolation, spike.t[0], spike.t_spike)
            root2 = scipy.optimize.brentq(U_interpolation, spike.t_spike, spike.t[-1])

            sum_AP_width += abs(root2 - root1)

        return None, sum_AP_width/float(self.spikes.nr_spikes)


    def accomondation_index(self, t, U):
        N = self.spikes.nr_spikes
        if N <= 1:
            return None, None

        k = min(4, int(round(N-1)/5.))

        ISIs = []
        for i in range(N-1):
            ISIs.append(self.spikes[i+1].t_spike - self.spikes[i].t_spike)

        A = 0
        for i in range(k+1, N-1):
            A += (ISIs[i] - ISIs[i-1])/(ISIs[i] + ISIs[i-1])
        return None, A/(N - k - 1)