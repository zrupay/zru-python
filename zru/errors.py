import sys


class ZRUError(Exception):
    """
    ZRU Error - class used to manage the exceptions related with zru library
    """
    def __init__(self, message=None, json_body=None, resource=None, resource_id=None):
        """
        Initializes an error
        :param message: Error type
        :param json_body: Response from server
        :param resource: Class resource used when the error raised
        :param resource_id: Resource id requested when the error raised
        """
        super(ZRUError, self).__init__(message)

        self._message = message
        self.json_body = json_body
        self.resource = resource
        self.resource_id = resource_id

    def __unicode__(self):
        """
        :return: Error type and response
        """
        return u"{0} {1}".format(self._message, self.json_body)

    if sys.version_info > (3, 0):
        def __str__(self):
            """
            Python >3
            :return: Unicode representation
            """
            return self.__unicode__()
    else:
        def __str__(self):
            """
            Python <3
            :return: Unicode representation
            """
            return unicode(self).encode('utf-8')


class InvalidRequestError(ZRUError):
    """
    Invalid request error
    """
    pass


class BadUseError(ZRUError):
    """
    Bad use error
    """
    pass
