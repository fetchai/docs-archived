.. _advanced-topics:

Using `async` APIs
==================

Alongside :func:`~oef.agents.Agent.connect`, :func:`~oef.agents.Agent.disconnect`, :func:`~oef.agents.Agent.run`,
:func:`~oef.agents.Agent.on_message` methods described in the previous sections, the SDK supports also the
*asynchronous counterparts* of those methods.

The naming convention is ``async_<method>``, where ``<method>`` is the name of the synchronous blocking function.
E.g. the ``async`` version of :func:`~oef.agents.Agent.connect` is :func:`~oef.agents.Agent.async_connect`,
the ``async`` version of :func:`~oef.agents.Agent.on_message` is :func:`~oef.core.DialogueInterface.async_on_message`,
 and so on.

The ``async`` callbacks might be useful when there is the need to run the code in asynchronous context.
