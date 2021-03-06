
class BaseHandler(object):
    """ Interface class to define base methods for a result handler
    class """

    def get_result(self, identifier):
        """ Returns the value of a result
        given its identifier """
        raise NotImplementedError

    def get_all_results(self):
        """ Returns a dictionary of all job identifiers mapped to
        their respective results """
        raise NotImplementedError

    def get_successful_runs(self):
        """ Returns a list of the identifiers of all
        successful runs """
        raise NotImplementedError

    def get_failed_runs(self):
        """ Returns a dictionary of error types mapped to
        lists of job identifiers which result in them """
        raise NotImplementedError

    def delete_result(self, identifier):
        """ Deletes a result entry given its identifier """
        raise NotImplementedError

    def delete_all_results(self):
        """ Deletes all result entries """
        raise NotImplementedError

    def ran_successfully(self, identifier):
        """ Returns true / false on whether the result with this
        identifier is successful """
        raise NotImplementedError

    def count_results(self):
        """ Returns the total number of results """
        raise NotImplementedError

    def count_successes(self):
        """ Returns the number of successful results """
        raise NotImplementedError

    def count_failures(self):
        """ Returns the number of failed results """
        raise NotImplementedError

    def insert_success(self, identifier):
        """ Adds a successful result """
        raise NotImplementedError

    def insert_failure(self, identifier, error_type):
        """ Adds a failed result """
        raise NotImplementedError
