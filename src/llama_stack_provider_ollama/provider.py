from llama_stack.providers.datatypes import ProviderSpec, Api, AdapterSpec, remote_provider_spec

def get_provider_spec() -> ProviderSpec:
    return remote_provider_spec(
        api=Api.inference,
        adapter=AdapterSpec(
            adapter_type="custom_ollama",
            pip_packages=["ollama", "aiohttp"],
            config_class="config.OllamaImplConfig",
            module="ollama_adapter",
        ),
    )
