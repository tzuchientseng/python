class StatTables:
    z_table = {
        80.0: 1.28,
        85.0: 1.44,
        90.0: 1.644853627,
        95.0: 1.959963985,
        98.0: 2.326347874,
        99.0: 2.575829304,
        99.8: 3.090232306,
        99.9: 3.2905267314,
    }

    t_table = {
        80.0: {i + 1: val for i, val in enumerate([
            3.078, 1.886, 1.638, 1.533, 1.476, 1.440, 1.415, 1.397, 1.383, 1.372, 1.363, 1.356, 1.350,
            1.345, 1.341, 1.337, 1.333, 1.330, 1.328, 1.325, 1.323, 1.321, 1.319, 1.318, 1.316, 1.315,
            1.314, 1.313, 1.311, 1.310, 1.303, 1.296, 1.289, 1.282
        ])},
        # Additional entries for other confidence levels should be added here similarly.
    }

    l_chi_square = {
        # Define LChiSquare dictionary similarly as in Java
    }

    r_chi_square = {
        # Define RChiSquare dictionary similarly as in Java
    }

    f_values = {
        # Define F-values dictionary similarly as in Java
    }

    @staticmethod
    def get_z_value(confidence_level):
        return StatTables.z_table.get(confidence_level, 1.96)

    @staticmethod
    def get_t_value(confidence_level, sample_size):
        try:
            return StatTables.t_table[confidence_level][sample_size]
        except KeyError:
            raise ValueError("T-value not found for the given confidence level and sample size")

    @staticmethod
    def get_l_chi_value(confidence_level, degrees_of_freedom):
        try:
            return StatTables.l_chi_square[confidence_level][degrees_of_freedom]
        except KeyError:
            raise ValueError("Left Chi-square value not found for the given confidence level and degrees of freedom")

    @staticmethod
    def get_r_chi_value(confidence_level, degrees_of_freedom):
        try:
            return StatTables.r_chi_square[confidence_level][degrees_of_freedom]
        except KeyError:
            raise ValueError("Right Chi-square value not found for the given confidence level and degrees of freedom")

    @staticmethod
    def get_f_value(confidence_level, df1, df2):
        try:
            return StatTables.f_values[confidence_level][df1][df2]
        except KeyError:
            raise ValueError("F-distribution value not found for the specified degrees of freedom and confidence level")
