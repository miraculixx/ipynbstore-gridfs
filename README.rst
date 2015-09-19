IPynbstore\_GridFS
==================

IPython Notebook Manager with GridFS Backend

Setting up
----------

**To Install**

::

    pip install ipynbstore_gridfs

Now, in your ipython config, configure the following.

**Required**

::

    c.NotebookApp.contents_manager_class='ipynbstore_gridfs.GridFSContentsManager'
    c.NotebookApp.GridFSContentsManager.mongo_uri='mongodb://localhost:27017/myDB'

**Note:** ``mongo_uri`` needs to be the full url of the mongo instance,
the plugin takes in db, user, pass and all other necessary variables
from the uri itself.
