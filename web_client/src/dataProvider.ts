import { AxiosInstance } from "axios";
import { stringify } from "query-string";
import { DataProvider } from "@pankod/refine-core";
import {
  generateFilter,
  generateSort,
  axiosInstance,
} from "@pankod/refine-simple-rest";


const dataProvider = (
  apiUrl: string,
  httpClient: AxiosInstance = axiosInstance
): Omit<
  Required<DataProvider>,
  "createMany" | "updateMany" | "deleteMany"
> => ({
  getList: async ({
    resource,
    hasPagination = true,
    pagination = { current: 1, pageSize: 10 },
    filters,
    sort,
  }) => {
    const url = `${apiUrl}/${resource}`;

    const { current = 1, pageSize = 10 } = pagination ?? {};

    const queryFilters = generateFilter(filters);

    const query: {
      skip?: number;
      limit?: number;
      _sort?: string;
      _order?: string;
    } = hasPagination
      ? {
          skip: (current - 1) * pageSize,
          limit: pageSize,
        }
      : {};

    const generatedSort = generateSort(sort);
    if (generatedSort) {
      const { _sort, _order } = generatedSort;
      query._sort = _sort.join(",");
      query._order = _order.join(",");
    }

    const { data, headers } = await httpClient.get(
      `${url}?${stringify(query)}`
    );

    const total = +headers["x-total-count"];

    return {
      data,
      total,
    };
  },

  getMany: async ({ resource, ids }) => {
    const { data } = await httpClient.get(
      `${apiUrl}/${resource}?${stringify({ id: ids })}`
    );

    return {
      data,
    };
  },

  create: async ({ resource, variables }) => {
    const url = `${apiUrl}/${resource}`;

    const { data } = await httpClient.post(url, variables);

    return {
      data,
    };
  },

  update: async ({ resource, id, variables }) => {
    const url = `${apiUrl}/${resource}`;

    const { data } = await httpClient.put(url, { ...variables, id });

    return {
      data,
    };
  },

  getOne: async ({ resource, id }) => {
    const url = `${apiUrl}/${resource}/${id}`;

    const { data } = await httpClient.get(url);

    return {
      data,
    };
  },

  deleteOne: async ({ resource, id, variables }) => {
    const url = `${apiUrl}/${resource}/${id}`;

    const { data } = await httpClient.delete(url, {
      data: variables,
    });

    return {
      data,
    };
  },

  getApiUrl: () => {
    return apiUrl;
  },

  custom: async ({ url, method, filters, sort, payload, query, headers }) => {
    let requestUrl = `${url}?`;

    if (sort) {
      const generatedSort = generateSort(sort);
      if (generatedSort) {
        const { _sort, _order } = generatedSort;
        const sortQuery = {
          _sort: _sort.join(","),
          _order: _order.join(","),
        };
        requestUrl = `${requestUrl}&${stringify(sortQuery)}`;
      }
    }

    if (filters) {
      const filterQuery = generateFilter(filters);
      requestUrl = `${requestUrl}&${stringify(filterQuery)}`;
    }

    if (query) {
      requestUrl = `${requestUrl}&${stringify(query)}`;
    }

    if (headers) {
      httpClient.defaults.headers = {
        ...httpClient.defaults.headers,
        ...headers,
      };
    }

    let axiosResponse;
    switch (method) {
      case "put":
      case "post":
      case "patch":
        axiosResponse = await httpClient[method](url, payload);
        break;
      case "delete":
        axiosResponse = await httpClient.delete(url, {
          data: payload,
        });
        break;
      default:
        axiosResponse = await httpClient.get(requestUrl);
        break;
    }

    const { data } = axiosResponse;

    return Promise.resolve({ data });
  },
});

export default dataProvider;
