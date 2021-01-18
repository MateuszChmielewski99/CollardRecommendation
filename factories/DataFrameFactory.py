from dataframe import df
from columns import genres_columns


class DataFrameFactory:
    def create_data_frames_array(self, first: bool, second: bool, third: bool):

        if not first and not second and not third:
            return [df.copy()]

        if first and not second and not third:
            return self.__get_divided_by_single_genre(genres_columns[0])
        if not first and second and not third:
            return self.__get_divided_by_single_genre(genres_columns[1])
        if not first and not second and third:
            return self.__get_divided_by_single_genre(genres_columns[2])
        if first and second and third:
            return self.__get_divided_by_three_genre(genres_columns[0], genres_columns[1], genres_columns[2])
        if first and second and not third:
            return self.__get_divided_by_two_genre(genres_columns[0], genres_columns[1])
        if first and not second and third:
            return self.__get_divided_by_two_genre(genres_columns[0], genres_columns[2])
        if not first and second and third:
            return self.__get_divided_by_two_genre(genres_columns[1], genres_columns[2])

    def __get_divided_by_single_genre(self, genre: str):
        grouped = df.groupby(df[genre])
        return self.__get_groupes_datasets(genre, grouped)

    def __get_divided_by_two_genre(self, first, second):
        df['tmp'] = df[first] + df[second]
        grouped = df.groupby(df['tmp'])
        result = self.__get_groupes_datasets('tmp', grouped)
        del df['tmp']
        return result

    def __get_divided_by_three_genre(self, first, second, third):
        df['tmp'] = df[first] + df[second] + df[third]
        grouped = df.groupby(df['tmp'])
        result = self.__get_groupes_datasets('tmp', grouped)
        del df['tmp']
        return result

    def __get_groupes_datasets(self, column_name, grouped):
        unique = df[column_name].unique()
        subsets = []
        for i in range(unique.size):
            subsets.append(grouped.get_group(unique[i]).copy())
        return subsets
